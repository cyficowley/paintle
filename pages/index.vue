<template>
  <div class="h-screen flex flex-col overscroll-none">
    <Header
      class="mb-4"
      :won="won"
      :lost="lost"
      @directions="showDirections = true"
      @winner="winPopup = true"
      @loser="losePopup = true"
    />
    <div class="container mx-auto flex-grow min-h-0">
      <Painting
        :painting="selectedAnswer"
        :changeable="!won"
        @revealed="handleReveal"
      />
    </div>
    <div class="container mx-auto grid grid-cols-12 px-2 gap-4 py-2 sm:py-4">
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

export default Vue.extend({
  name: 'IndexPage',
  data() {
    return {
      possibleAnswers: [
        {
          artist: 'Johannes Vermeer',
          name: 'Girl with a Pearl Earring',
          path: '/paintings/girl.webp',
        },
        {
          artist: 'Salvador Dali',
          name: 'The Persistence of Memory',
          path: '/paintings/persistence.webp',
        },
        {
          artist: 'Edvard Munch',
          name: 'The Scream',
          path: '/paintings/scream.webp',
        },
        {
          artist: 'Vincent van Gogh',
          name: 'Starry Night',
          path: '/paintings/starry.webp',
        },
        {
          artist: 'Pablo Picaso',
          name: 'Guernica',
          path: '/paintings/guernica.webp',
        },
        {
          artist: 'Jan Van Eyck',
          name: 'The Arnolfini Portrait',
          path: '/paintings/Arnolfini-portrait.webp',
        },
        {
          artist: 'Sandro Botticelli',
          name: 'The Birth of Venus',
          path: '/paintings/birth-of-venus.webp',
        },
        {
          artist: 'Raphael',
          name: 'The School of Athens',
          path: '/paintings/school-of-athens.webp',
        },
        {
          artist: 'Michelangelo',
          name: 'The Sistine Chapel Ceiling',
          path: '/paintings/sistine-chapel.webp',
        },
        {
          artist: 'Caravaggio',
          name: 'The Calling of Saint Matthew',
          path: '/paintings/calling-of-saint-matthew.webp',
        },
        {
          artist: 'Diego Velázquez',
          name: 'Las Meninas',
          path: '/paintings/las-meninas.webp',
        },
        {
          artist: 'Leonardo da Vinci',
          name: 'Mona Lisa',
          path: '/paintings/mona.webp',
        },
        {
          artist: 'Rembrandt van Rijn',
          name: 'The Night Watch',
          path: '/paintings/nightwatch.webp',
        },
        {
          artist: 'Jean-Honoré Fragonard',
          name: 'The Swing',
          path: '/paintings/the-swing.webp',
        },
        {
          artist: 'Jacque-Louis David',
          name: 'Napoleon Crossing the Alps',
          path: '/paintings/napoleon-crossing-the-alps.webp',
        },
        {
          artist: 'Théodore Géricault',
          name: 'The Raft of The Medusa',
          path: '/paintings/raft-of-medusa.webp',
        },
        {
          artist: 'Eugène Delacroix',
          name: 'Liberty Leading the People',
          path: '/paintings/delacroix-liberty.webp',
        },
        {
          artist: 'James McNeill Whistler',
          name: "Whistler's Mother",
          path: '/paintings/whistler-mother.webp',
        },
        {
          artist: 'Edouard Manet',
          name: "Le Dejeuner sur l'Herbe",
          path: '/paintings/dejeuner.webp',
        },
        {
          artist: 'Edouard Manet',
          name: 'A Bar at the Folies-Bergere',
          path: '/paintings/a-bar-at-the-folies-bergere.webp',
        },
        {
          artist: 'Claude Monet',
          name: 'Sunrise',
          path: '/paintings/sunrise.webp',
        },
        {
          artist: 'Pierre-Auguste Renoir',
          name: 'Bal du Moulin de la Galette',
          path: '/paintings/bal-du-moulin.webp',
        },
        {
          artist: 'Georges Seurat',
          name: 'A Sunday Afternoon on the Island of La Grande Jatte',
          path: '/paintings/sunday-afternoon.webp',
        },
        {
          artist: 'Gustav Klimt',
          name: 'The Kiss',
          path: '/paintings/the-kiss.webp',
        },
        {
          artist: 'Pablo Picasso',
          name: "Les Demoiselles d'Avignon",
          path: '/paintings/demoiselles.webp',
        },
        {
          artist: 'Marcel Duchamp',
          name: 'Nude Descending a Staircase',
          path: '/paintings/nude-staircase.webp',
        },
        {
          artist: 'Grant Wood',
          name: 'American Gothic',
          path: '/paintings/american-gothic.webp',
        },
        {
          artist: 'Edward Hopper',
          name: 'Nighthawks',
          path: '/paintings/nighthawks.webp',
        },
        {
          artist: 'Rene Magritte',
          name: "The Treachery of Images (Ceci N'est Pas Une Pipe)",
          path: '/paintings/pipe.webp',
        },
      ],
      selectedAnswer: {
        artist: 'Pablo Picaso',
        name: 'Guernica',
        path: '/paintings/guernica.webp',
      },
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
  created() {
    const startDate = new Date(2022, 3, 17) // day that we wrote this code
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
