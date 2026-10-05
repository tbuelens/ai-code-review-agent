<script setup>
import { ref, onMounted } from 'vue'
import { checkHealth, analyzeCode } from './services/api.js'

import AppHeader from './components/AppHeader.vue'
import CodeEditor from './components/CodeEditor.vue'
import LoadingState from './components/LoadingState.vue'
import AnalysisPanel from './components/AnalysisPanel.vue'
import RefactoringPanel from './components/RefactoringPanel.vue'
import ReviewPanel from './components/ReviewPanel.vue'

const DEFAULT_CODE = 'def divide(a, b):\n    return a / b\n'

const language = ref('python')
const code = ref(DEFAULT_CODE)

const isLoading = ref(false)
const errorMessage = ref('')

// Populated only after a successful /analyze response.
const analysisResult = ref(null)
const refactoringResult = ref(null)
const reviewResult = ref(null)

// Snapshot of the code that was actually submitted, so the refactoring
// panel always shows "before" code matching the result it's paired with,
// even if the user keeps editing the textarea afterwards.
const submittedCode = ref('')

// 'checking' | 'online' | 'offline'
const apiStatus = ref('checking')

async function runHealthCheck() {
  apiStatus.value = 'checking'
  const isHealthy = await checkHealth()
  apiStatus.value = isHealthy ? 'online' : 'offline'
}

async function handleAnalyze() {
  if (isLoading.value || code.value.trim().length === 0) return

  isLoading.value = true
  errorMessage.value = ''

  try {
    const result = await analyzeCode(language.value, code.value)
    analysisResult.value = result.analysis
    refactoringResult.value = result.refactoring
    reviewResult.value = result.review
    submittedCode.value = code.value
  } catch (error) {
    errorMessage.value = error.message || 'Something went wrong while analyzing the code.'
    // Keep showing results from a previous successful run is misleading for
    // a failed request, so clear them out.
    analysisResult.value = null
    refactoringResult.value = null
    reviewResult.value = null
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  runHealthCheck()
})
</script>

<template>
  <AppHeader :api-status="apiStatus" />

  <main class="app-main">
    <CodeEditor
      v-model:language="language"
      v-model:code="code"
      :is-loading="isLoading"
      @analyze="handleAnalyze"
    />

    <p v-if="errorMessage" class="error-banner" role="alert">
      {{ errorMessage }}
    </p>

    <LoadingState v-if="isLoading" />

    <template v-if="!isLoading && analysisResult">
      <AnalysisPanel :analysis="analysisResult" />
      <RefactoringPanel :original-code="submittedCode" :refactoring="refactoringResult" />
      <ReviewPanel :review="reviewResult" />
    </template>
  </main>
</template>

<style scoped>
.app-main {
  max-width: 1100px;
  margin: 0 auto;
  padding: 28px 32px 64px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.error-banner {
  margin: 0;
  padding: 12px 16px;
  border: 1px solid rgba(248, 81, 73, 0.3);
  background-color: var(--color-danger-bg);
  color: var(--color-danger);
  border-radius: var(--radius);
  font-size: 14px;
}

@media (max-width: 640px) {
  .app-main {
    padding: 20px 16px 48px;
  }
}
</style>
