<template>
  <div class="quizHeader">
    <b-nav tabs>
      <b-nav-item disabled>Fancy Quiz App</b-nav-item>
      <b-nav-item disabled>
        Right/Total:
        <b-badge pill variant="success">{{ correctCount }}</b-badge>
        <b-badge pill variant="danger">{{ total }}</b-badge>
      </b-nav-item>
      <b-nav-item disabled>
        Current Index:
        <b-badge pill variant="info">{{ currentIndex }}</b-badge>
      </b-nav-item>
    </b-nav>
  </div>
</template>

<script>
export default {
  props: {
    total: Number,
    correctCount: Number,
    currentIndex: Number
  }
};
</script>
