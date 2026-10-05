<script setup>
defineProps({
  originalCode: {
    type: String,
    required: true,
  },
  // RefactoringResult shape: { refactored_code, changes, explanation }
  refactoring: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section class="card refactoring-panel">
    <h2 class="section-title">Refactoring</h2>

    <div class="code-columns">
      <div class="code-column">
        <h3 class="code-column__label">Original Code</h3>
        <pre class="code-block"><code>{{ originalCode }}</code></pre>
      </div>
      <div class="code-column">
        <h3 class="code-column__label">Refactored Code</h3>
        <pre class="code-block"><code>{{ refactoring.refactored_code }}</code></pre>
      </div>
    </div>

    <div class="refactoring-details">
      <div>
        <h3 class="code-column__label">Changes</h3>
        <p v-if="refactoring.changes.length === 0" class="empty-state">
          No specific changes were listed.
        </p>
        <ul v-else class="change-list">
          <li v-for="(change, index) in refactoring.changes" :key="index">{{ change }}</li>
        </ul>
      </div>

      <div>
        <h3 class="code-column__label">Explanation</h3>
        <p class="explanation-text">{{ refactoring.explanation }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.refactoring-panel {
  padding: 20px;
}

.code-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}

@media (max-width: 860px) {
  .code-columns {
    grid-template-columns: 1fr;
  }
}

.code-column {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 0;
}

.code-column__label {
  margin: 0;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--color-text-muted);
}

.code-block {
  margin: 0;
  background-color: var(--color-bg-elevated);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius);
  padding: 14px;
  font-size: 13px;
  line-height: 1.6;
  white-space: pre;
  overflow-x: auto;
  max-height: 420px;
}

.refactoring-details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 860px) {
  .refactoring-details {
    grid-template-columns: 1fr;
  }
}

.empty-state {
  margin: 0;
  color: var(--color-text-muted);
  font-size: 14px;
}

.change-list {
  margin: 0;
  padding-left: 20px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--color-text);
}

.explanation-text {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
  color: var(--color-text);
  white-space: pre-wrap;
}
</style>
