<script setup>
defineProps({
  // 'checking' | 'online' | 'offline'
  apiStatus: {
    type: String,
    required: true,
  },
})

const statusLabels = {
  checking: 'Checking...',
  online: 'Online',
  offline: 'Offline',
}
</script>

<template>
  <header class="app-header">
    <div class="app-header__titles">
      <h1>AI Code Review Agent</h1>
      <p class="app-header__subtitle">Analyze. Refactor. Review.</p>
    </div>

    <div class="app-header__status" :class="`app-header__status--${apiStatus}`">
      <span class="status-dot"></span>
      <span>API {{ statusLabels[apiStatus] }}</span>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 32px;
  border-bottom: 1px solid var(--color-border);
  background-color: var(--color-bg-elevated);
}

.app-header__titles h1 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  letter-spacing: -0.01em;
}

.app-header__subtitle {
  margin: 2px 0 0;
  font-size: 13px;
  color: var(--color-text-muted);
}

.app-header__status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid var(--color-border);
  background-color: var(--color-surface);
  color: var(--color-text-muted);
  white-space: nowrap;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--color-text-dim);
}

.app-header__status--online {
  color: var(--color-success);
  border-color: rgba(63, 185, 80, 0.3);
}
.app-header__status--online .status-dot {
  background-color: var(--color-success);
}

.app-header__status--offline {
  color: var(--color-danger);
  border-color: rgba(248, 81, 73, 0.3);
}
.app-header__status--offline .status-dot {
  background-color: var(--color-danger);
}

.app-header__status--checking .status-dot {
  background-color: var(--color-warning);
}

@media (max-width: 640px) {
  .app-header {
    flex-direction: column;
    align-items: flex-start;
    padding: 16px 20px;
  }
}
</style>
