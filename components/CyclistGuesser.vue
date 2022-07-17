<template>
  <div class="relative w-full bg-white sm:flex">
    <!-- <p>guess is: {{ guess }}</p> -->
    <div class="absolute top-0 w-full">
      <Results
        v-if="guess.length > 2 && !canSubmit"
        :results="filteredCyclists"
        :has-artist="false"
        class="absolute bottom-0 w-full mb-2"
        @selected="setGuess"
      />
    </div>
    <input
      v-model="guess"
      type="text"
      :placeholder="placeholderText"
      :disabled="!canGuess"
      class="flex-grow w-full px-3 py-3 mb-2 text-xl text-gray-500 border-4 outline-none  border-bluey rounded-2xl sm:text-2xl sm:px-4 sm:py-3 sm:mb-0"
      @keyup.enter="checkEnter"
    />
    <button
      v-if="wrongGuess"
      class="w-full px-3 py-3 text-xl text-white outline-none  rounded-2xl sm:text-2xl sm:ml-4 sm:px-4 sm:w-auto sm:py-3 bg-redd"
      @click="canGuess ? guessed() : null"
    >
      Incorrect
    </button>
    <button
      v-else
      class="w-full px-3 py-3 text-xl text-white outline-none  sm:text-2xl sm:ml-4 sm:px-4 sm:py-4 sm:w-auto rounded-2xl"
      :class="canSubmit ? 'hover:bg-bluey-dark bg-bluey' : 'bg-bluey-light'"
      @click="canGuess ? guessed() : null"
    >
      Submit
    </button>
    <div v-if="revealed.length == 17" class="">
      <button
        class="w-full px-3 py-3 mt-2 text-xl text-white outline-none  sm:mt-0 rounded-2xl sm:text-2xl sm:ml-4 sm:px-4 sm:py-3 bg-redd"
        @click="$emit('loser')"
      >
        Idk
      </button>
    </div>
  </div>
</template>


<script>
export default {
  name: 'CyclistGuesserItem',
  props: {
    allAnswers: {
      type: Array,
      required: true,
    },
    canGuess: {
      type: Boolean,
      required: true,
    },
    wrongGuess: {
      type: Boolean,
      required: true,
    },
    won: {
      type: Boolean,
      required: true,
    },
    lost: {
      type: Boolean,
      required: true,
    },
    revealed: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      guess: '',
      results: [],
    }
  },
  computed: {
    filteredCyclists() {
      const filteredCyclists = this.allAnswers.filter((painting) => {
        return painting.name.toLowerCase().includes(this.guess.toLowerCase())
      })
      return filteredCyclists
    },
    canSubmit() {
      return (
        this.canGuess &&
        this.allAnswers.some((painting) => {
          return painting.name.toLowerCase() === this.guess.toLowerCase()
        })
      )
    },
    placeholderText() {
      if (this.won) {
        return 'You won!'
      }
      if (this.lost) {
        return 'You lost :('
      }
      if (this.canGuess) {
        return 'Search for cyclist'
      }
      return 'Please select a tile to reveal'
    },
  },
  methods: {
    setGuess(guess) {
      this.guess = guess.name
    },
    guessed() {
      this.$emit('guessed', this.guess)
      this.guess = ''
    },
    checkEnter() {
      if (this.filteredCyclists.length === 1) {
        this.guess = this.filteredCyclists[0].name
      }
      if (this.canSubmit) {
        this.guessed()
      }
    },
  },
}
</script>
