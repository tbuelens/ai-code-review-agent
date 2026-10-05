<script setup>
defineProps({
  // ReviewResult shape: { approved, feedback, remaining_issues }
  review: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section class="card review-panel">
    <h2 class="section-title">Review</h2>

    <div class="status-badge" :class="review.approved ? 'status-badge--approved' : 'status-badge--rejected'">
      {{ review.approved ? 'APPROVED' : 'REJECTED' }}
    </div>

    <div class="review-field">
      <h3 class="review-field__label">Reviewer Feedback</h3>
      <p class="review-field__text">{{ review.feedback }}</p>
    </div>

    <div class="review-field">
      <h3 class="review-field__label">Remaining Issues</h3>
      <p v-if="review.remaining_issues.length === 0" class="empty-state">
        No remaining issues were reported.
      </p>
      <ul v-else class="remaining-issues-list">
        <li v-for="(issue, index) in review.remaining_issues" :key="index">{{ issue }}</li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.review-panel {
  padding: 20px;
}

.status-badge {
  display: inline-block;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.05em;
  padding: 6px 16px;
  border-radius: 999px;
  margin-bottom: 16px;
}

.status-badge--approved {
  color: var(--color-success);
  background-color: var(--color-success-bg);
  border: 1px solid rgba(63, 185, 80, 0.3);
}

.status-badge--rejected {
  color: var(--color-danger);
  background-color: var(--color-danger-bg);
  border: 1px solid rgba(248, 81, 73, 0.3);
}

.review-field {
  margin-top: 16px;
}

.review-field__label {
  margin: 0 0 6px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--color-text-muted);
}

.review-field__text {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
  color: var(--color-text);
  white-space: pre-wrap;
}

.empty-state {
  margin: 0;
  color: var(--color-text-muted);
  font-size: 14px;
}

.remaining-issues-list {
  margin: 0;
  padding-left: 20px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--color-text);
}
</style>
