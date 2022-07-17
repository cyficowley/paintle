<template>
  <div class="flex flex-col h-screen overscroll-none">
    <CyclistHeader
      class="mb-4"
      :won="won"
      :lost="lost"
      @directions="showDirections = true"
      @winner="winPopup = true"
      @loser="losePopup = true"
    />
    <div class="container flex-grow min-h-0 mx-auto">
      <CyclistPainting
        :painting="selectedAnswer"
        :changeable="!won"
        :reveal="won || lost"
        @revealed="handleReveal"
      />
    </div>
    <div class="container grid grid-cols-12 gap-4 px-2 py-2 mx-auto sm:py-4">
      <CyclistGuesser
        :all-answers="possibleAnswers"
        :can-guess="canGuess && !won"
        :revealed="revealed"
        class="col-span-12 sm:col-span-8 sm:col-start-3"
        :wrong-guess="wrongGuess"
        :won="won"
        :lost="lost"
        @guessed="handleGuess"
        @loser="handleLoser"
      />
    </div>
    <Popup :visible="showDirections" @close="showDirections = false">
      <CyclistDirections />
    </Popup>
    <Popup :visible="winPopup" @close="winPopup = false">
      <CyclistWinner :guesses="revealed" />
    </Popup>
    <Popup :visible="losePopup" @close="losePopup = false">
      <CyclistLoser :guesses="revealed" :answer="selectedAnswer" />
    </Popup>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import paintings from '../static/cyclist_paintings.json'
import CyclistDirections from '~/components/CyclistDirections.vue'

export default Vue.extend({
  name: 'CyclistPage',
  components: { CyclistDirections },
  data() {
    const possibleAnswers = paintings.paintings
    const index = Math.floor(Math.random() * possibleAnswers.length)
    const selectedAnswer = possibleAnswers[index]
    const shuffledAnswers = [...possibleAnswers]
    for (let i = shuffledAnswers.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[shuffledAnswers[i], shuffledAnswers[j]] = [
        shuffledAnswers[j],
        shuffledAnswers[i],
      ]
    }
    return {
      selectedAnswer,
      possibleAnswers: shuffledAnswers,
      canGuess: false,
      revealed: [-1],
      showDirections: false,
      winPopup: false,
      losePopup: false,
      won: false,
      lost: false,
      wrongGuess: false,
    }
  },
  methods: {
    handleGuess(guess: string) {
      this.canGuess = false
      if (this.selectedAnswer.name.toLowerCase() === guess.toLowerCase()) {
        this.won = true
        this.winPopup = true
      } else {
        this.wrongGuess = true
        setTimeout(() => {
          this.wrongGuess = false
        }, 3000)
      }
    },
    handleReveal(revealLocation: number) {
      if (!this.revealed.includes(revealLocation)) {
        this.revealed.push(revealLocation)
      }
      this.canGuess = true
    },
    handleLoser() {
      this.losePopup = true
      this.canGuess = false
      this.lost = true
    },
  },
})
</script>
