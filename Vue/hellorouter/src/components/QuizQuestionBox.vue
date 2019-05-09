<template>
  <div>
    <b-jumbotron>
      <template slot="lead">Q: {{currentQuestion.question}}</template>

      <hr class="my-4">

      <b-list-group>
        <b-list-group-item>Cras justo odio</b-list-group-item>
        <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
        <b-list-group-item>Morbi leo risus</b-list-group-item>
        <b-list-group-item>Porta ac consectetur ac</b-list-group-item>
      </b-list-group>

      <b-button variant="outline-primary" href="#">Summit</b-button>
      <b-button v-on:click="pre" variant="outline-info" href="#">Pre</b-button>
      <b-button v-on:click="next" variant="outline-info" href="#">Next</b-button>
    </b-jumbotron>
  </div>
</template>

<script>
export default {
  props: {
    currentQuestion: Object,
    pre: Function,
    next: Function
  }
}
</script>