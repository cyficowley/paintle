<template>
  <div class="relative bg-white sm:flex w-full">
    <!-- <p>guess is: {{ guess }}</p> -->
    <div class="absolute w-full top-0">
      <Results
        v-if="guess.length > 2 && !canSubmit"
        :results="filteredPaintings"
        class="absolute w-full bottom-0 mb-2"
        @selected="setGuess"
      />
    </div>
    <input
      v-model="guess"
      type="text"
      :placeholder="placeholderText"
      :disabled="!canGuess"
      class="
        border-4 border-bluey
        rounded-2xl
        text-xl
        sm:text-2xl
        outline-none
        w-full
        sm:px-4
        px-3
        sm:py-3
        py-3
        flex-grow
        text-gray-500
        mb-2
        sm:mb-0
      "
      @keyup.enter="checkEnter"
    />
    <button
      v-if="wrongGuess"
      class="
        rounded-2xl
        text-xl
        sm:text-2xl
        outline-none
        sm:ml-4 sm:px-4
        px-3
        w-full
        sm:w-auto sm:py-3
        py-3
        text-white
        bg-redd
      "
      @click="canGuess ? guessed() : null"
    >
      Incorrect
    </button>
    <button
      v-else
      class="
        text-xl
        sm:text-2xl
        outline-none
        sm:ml-4 sm:px-4
        px-3
        sm:py-4
        py-3
        w-full
        sm:w-auto
        rounded-2xl
        text-white
      "
      :class="canSubmit ? 'hover:bg-bluey-dark bg-bluey' : 'bg-bluey-light'"
      @click="canGuess ? guessed() : null"
    >
      Submit
    </button>
    <div v-if="revealed.length == 17" class="">
      <button
        class="
          mt-2
          sm:mt-0
          rounded-2xl
          text-xl
          sm:text-2xl
          outline-none
          w-full
          sm:ml-4 sm:px-4
          px-3
          sm:py-3
          py-3
          text-white
          bg-redd
        "
        @click="$emit('loser')"
      >
        Idk
      </button>
    </div>
  </div>
</template>


<script>
export default {
  name: 'GuesserItem',
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
    filteredPaintings() {
      const filteredPaintings = this.allAnswers.filter((painting) => {
        return (
          painting.artist.toLowerCase().includes(this.guess.toLowerCase()) ||
          painting.name.toLowerCase().includes(this.guess.toLowerCase())
        )
      })
      return filteredPaintings
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
        return 'Search for artist / painting'
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
      if (this.filteredPaintings.length === 1) {
        this.guess = this.filteredPaintings[0].name
      }
      if (this.canSubmit) {
        this.guessed()
      }
    },
  },
}
</script>