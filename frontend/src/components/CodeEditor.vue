<script setup>
import { computed } from 'vue'

const props = defineProps({
  language: {
    type: String,
    required: true,
  },
  code: {
    type: String,
    required: true,
  },
  isLoading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['update:language', 'update:code', 'analyze'])

const SUPPORTED_LANGUAGES = [
  'python',
  'java',
  'javascript',
  'typescript',
  'php',
  'csharp',
  'cpp',
  'go',
]

const isAnalyzeDisabled = computed(() => props.isLoading || props.code.trim().length === 0)

function onLanguageChange(event) {
  emit('update:language', event.target.value)
}

function onCodeInput(event) {
  emit('update:code', event.target.value)
}

function onAnalyzeClick() {
  if (!isAnalyzeDisabled.value) {
    emit('analyze')
  }
}
</script>

<template>
  <section class="card editor-panel">
    <div class="editor-panel__row">
      <label class="field-label" for="language-select">Language</label>
      <select
        id="language-select"
        class="language-select"
        :value="language"
        :disabled="isLoading"
        @change="onLanguageChange"
      >
        <option v-for="lang in SUPPORTED_LANGUAGES" :key="lang" :value="lang">
          {{ lang }}
        </option>
      </select>
    </div>

    <label class="field-label" for="code-input">Source Code</label>
    <textarea
      id="code-input"
      class="code-input"
      :value="code"
      :disabled="isLoading"
      placeholder="Paste or write the code you want reviewed..."
      spellcheck="false"
      @input="onCodeInput"
    ></textarea>

    <div class="editor-panel__actions">
      <button
        type="button"
        class="analyze-button"
        :disabled="isAnalyzeDisabled"
        @click="onAnalyzeClick"
      >
        {{ isLoading ? 'Analyzing...' : 'Analyze Code' }}
      </button>
    </div>
  </section>
</template>

<style scoped>
.editor-panel {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.editor-panel__row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.field-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--color-text-muted);
}

.language-select {
  background-color: var(--color-bg-elevated);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 6px 10px;
  font-size: 14px;
  text-transform: capitalize;
}

.language-select:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.code-input {
  width: 100%;
  min-height: 260px;
  resize: vertical;
  background-color: var(--color-bg-elevated);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 14px;
  font-size: 13.5px;
  line-height: 1.6;
  white-space: pre;
  overflow: auto;
}

.code-input:focus {
  outline: none;
  border-color: var(--color-accent-muted);
}

.code-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.editor-panel__actions {
  display: flex;
  justify-content: flex-end;
}

.analyze-button {
  background-color: var(--color-accent-muted);
  color: #ffffff;
  border: 1px solid transparent;
  border-radius: var(--radius);
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.15s ease;
}

.analyze-button:hover:not(:disabled) {
  background-color: var(--color-accent);
}

.analyze-button:disabled {
  background-color: var(--color-surface-hover);
  color: var(--color-text-dim);
  cursor: not-allowed;
}
</style>
