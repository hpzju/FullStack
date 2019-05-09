<template>
  <div class="quiz">
    <b-container>
      <b-row align-h="center">
        <QuizHeader
          v-if="questions.length"
          :correctCount="count"
          :total="questions.length"
          :currentIndex="index+1"
        />
      </b-row>
      <b-row align-h="center">
        <QuizQuestionBox
          v-if="questions.length"
          v-bind:currentQuestion="questions[index]"
          :next="next"
          :pre="pre"
        />
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import QuizHeader from "@/components/QuizHeader.vue";
import QuizQuestionBox from "@/components/QuizQuestionBox.vue";

export default {
  name: "quiz",
  components: {
    QuizHeader,
    QuizQuestionBox
  },

  data() {
    return {
      questions: [],
      count: 0,
      index: 0
    };
  },
  methods: {
    next: function () {
      this.index = (this.index + 1) % 10
    },
    pre: function () {
      this.index = (this.index - 1 + 10) % 10
    }
  },
  mounted: function () {
    fetch("https://opentdb.com/api.php?amount=10&category=18&type=multiple", {
      method: "get"
    }).then((response) => {
      return response.json();
    }).then((jsonData) => {
      this.questions = jsonData.results
    })
  }
};
</script>
