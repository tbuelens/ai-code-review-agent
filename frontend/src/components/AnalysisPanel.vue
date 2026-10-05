<script setup>
defineProps({
  // CodeAnalysis shape: { issues: [{ severity, category, description }] }
  analysis: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section class="card analysis-panel">
    <h2 class="section-title">Analysis</h2>

    <p v-if="analysis.issues.length === 0" class="empty-state">
      No issues were found in the submitted code.
    </p>

    <ul v-else class="issue-list">
      <li v-for="(issue, index) in analysis.issues" :key="index" class="issue">
        <div class="issue__meta">
          <span class="severity-badge" :class="`severity-badge--${issue.severity}`">
            {{ issue.severity }}
          </span>
          <span class="issue__category">{{ issue.category.replace('_', ' ') }}</span>
        </div>
        <p class="issue__description">{{ issue.description }}</p>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.analysis-panel {
  padding: 20px;
}

.empty-state {
  margin: 0;
  color: var(--color-text-muted);
  font-size: 14px;
}

.issue-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.issue {
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius);
  padding: 12px 14px;
  background-color: var(--color-bg-elevated);
}

.issue__meta {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 6px;
}

.severity-badge {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 2px 8px;
  border-radius: 4px;
}

.severity-badge--high {
  color: var(--color-danger);
  background-color: var(--color-danger-bg);
}

.severity-badge--medium {
  color: var(--color-warning);
  background-color: var(--color-warning-bg);
}

.severity-badge--low {
  color: var(--color-text-muted);
  background-color: var(--color-surface-hover);
}

.issue__category {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: var(--color-text-muted);
}

.issue__description {
  margin: 0;
  font-size: 14px;
  color: var(--color-text);
  line-height: 1.5;
}
</style>
