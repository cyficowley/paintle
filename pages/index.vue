<template>
  <div class="flex flex-col h-screen overscroll-none">
    <Header
      class="mb-4"
      :won="won"
      :lost="lost"
      @directions="showDirections = true"
      @winner="winPopup = true"
      @loser="losePopup = true"
    />
    <div class="container flex-grow min-h-0 mx-auto">
      <Painting
        :painting="selectedAnswer"
        :changeable="!won"
        :reveal="won || lost"
        @revealed="handleReveal"
      />
    </div>
    <div class="container grid grid-cols-12 gap-4 px-2 py-2 mx-auto sm:py-4">
      <Guesser
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
      <Directions />
    </Popup>
    <Popup :visible="winPopup" @close="winPopup = false">
      <Winner :guesses="revealed" />
    </Popup>
    <Popup :visible="losePopup" @close="losePopup = false">
      <Loser :guesses="revealed" :answer="selectedAnswer" />
    </Popup>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import paintings from '../static/paintings.json'

export default Vue.extend({
  name: 'IndexPage',
  data() {
    const possibleAnswers = paintings.paintings

    console.log(possibleAnswers)

    const startDate = new Date(2022, 3, 19) // day that we wrote this code
    const now = new Date()

    // The days between the startDate and now
    const days = Math.floor(
      (now.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
    )

    const selectedAnswer = possibleAnswers[days % possibleAnswers.length]

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
