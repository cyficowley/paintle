<template>
  <div class="h-screen flex flex-col overscroll-none">
    <Header
      class="mb-4"
      :won="won"
      @directions="showDirections = true"
      @winner="winPopup = true"
    />
    <div class="container mx-auto flex-grow min-h-0">
      <Painting
        :painting="selectedAnswer"
        :changeable="!won"
        @revealed="handleReveal"
      />
    </div>
    <div class="container mx-auto grid grid-cols-12 gap-4 py-4">
      <Guesser
        :all-answers="possibleAnswers"
        :can-guess="canGuess && !won"
        class="col-span-8 col-start-3"
        @guessed="handleGuess"
      />
    </div>
    <Popup :visible="showDirections" @close="showDirections = false">
      <Directions />
    </Popup>
    <Popup :visible="winPopup" @close="winPopup = false">
      <Winner :guesses="revealed" />
    </Popup>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  data() {
    return {
      possibleAnswers: [
        {
          artist: 'Johannes Vermeer',
          name: 'Girl with a Peal Earring',
          path: '/paintings/girl.jpeg',
        },
        {
          artist: 'Leonardo da Vinci',
          name: 'Mona Lisa',
          path: '/paintings/mona.jpeg',
        },
        {
          artist: 'Salvador Dali',
          name: 'The Persistence of Memory',
          path: '/paintings/persistence.jpeg',
        },
        {
          artist: 'Edvard Munch',
          name: 'The Scream',
          path: '/paintings/scream.jpeg',
        },
        {
          artist: 'Vincent van Gogh',
          name: 'Starry Night',
          path: '/paintings/starry.jpeg',
        },
        {
          artist: 'Pablo Picaso',
          name: 'Guernica',
          path: '/paintings/guernica.jpeg',
        },
      ],
      selectedAnswer: {
        artist: 'Pablo Picaso',
        name: 'Guernica',
        path: '/paintings/guernica.jpeg',
      },
      canGuess: false,
      revealed: [-1],
      showDirections: false,
      winPopup: false,
      won: false,
    }
  },
  created() {
    const startDate = new Date(2022, 3, 16) // day that we wrote this code
    const now = new Date()

    // The days between the startDate and now
    const days = Math.floor(
      (now.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
    )

    this.selectedAnswer =
      this.possibleAnswers[days % this.possibleAnswers.length]
  },
  methods: {
    handleGuess(guess: string) {
      this.canGuess = false
      if (this.selectedAnswer.name.toLowerCase() === guess.toLowerCase()) {
        this.won = true
        this.winPopup = true
      }
    },
    handleReveal(revealLocation: number) {
      this.revealed.push(revealLocation)
      this.canGuess = true
    },
  },
})
</script>
