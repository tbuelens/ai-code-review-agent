<script setup>
// The backend only responds once the full workflow has finished, so we
// cannot show real per-stage progress. This component just communicates
// which stages exist, with a neutral pulsing animation - it never claims
// that a specific stage has completed.
const stages = ['Analyzer', 'Refactor', 'Reviewer']
</script>

<template>
  <section class="card loading-panel" role="status" aria-live="polite">
    <div class="loading-panel__stages">
      <template v-for="(stage, index) in stages" :key="stage">
        <div class="stage">
          <span class="stage__dot"></span>
          <span class="stage__label">{{ stage }}</span>
        </div>
        <span v-if="index < stages.length - 1" class="stage__arrow">&rarr;</span>
      </template>
    </div>
    <p class="loading-panel__hint">
      Running the multi-agent workflow. This can take a little while...
    </p>
  </section>
</template>

<style scoped>
.loading-panel {
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.loading-panel__stages {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  justify-content: center;
}

.stage {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border: 1px solid var(--color-border);
  border-radius: 999px;
  background-color: var(--color-bg-elevated);
}

.stage__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--color-accent);
  animation: pulse 1.3s ease-in-out infinite;
}

.stage:nth-child(3) .stage__dot {
  animation-delay: 0.2s;
}

.stage:nth-child(5) .stage__dot {
  animation-delay: 0.4s;
}

.stage__label {
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text);
}

.stage__arrow {
  color: var(--color-text-dim);
}

.loading-panel__hint {
  margin: 0;
  font-size: 13px;
  color: var(--color-text-muted);
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.35;
    transform: scale(0.85);
  }
  50% {
    opacity: 1;
    transform: scale(1.15);
  }
}
</style>
