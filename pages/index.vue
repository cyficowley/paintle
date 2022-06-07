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

export default Vue.extend({
  name: 'IndexPage',
  data() {
    const possibleAnswers = [
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
        artist: 'Jan Van Eyck',
        name: 'The Arnolfini Portrait',
        path: '/paintings/arnolfini-portrait.webp',
      },
      {
        artist: 'James McNeill Whistler',
        name: "Whistler's Mother",
        path: '/paintings/whistler-mother.webp',
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
      {
        artist: 'John William Waterhouse',
        name: 'The Magic Cicle',
        path: '/paintings/circle.webp',
      },
      {
        artist: 'Pieter Bruegel the Elder',
        name: 'The Tower Of Babel',
        path: '/paintings/babs.webp',
      },
      {
        artist: 'Vincent van Gogh',
        name: 'Fishing boats on the Beach at Les Saintes-Maries-de-la-Mer',
        path: '/paintings/boat.webp',
      },
      {
        artist: 'Hans Andersen Brendekilde',
        name: 'A wooded path in Autumn',
        path: '/paintings/wood.webp',
      },
      {
        artist: 'Francesco Paolo Hayez',
        name: 'The Kiss',
        path: '/paintings/kiss.webp',
      },
      {
        artist: 'Jacques-Louis David',
        name: 'Patroclus',
        path: '/paintings/patroclus.webp',
      },
      {
        artist: 'Leonardo Da Vinci',
        name: 'The Last Supper',
        path: '/paintings/supps.webp',
      },
      {
        artist: 'Vincent van Gogh',
        name: 'Café Terrace at Night',
        path: '/paintings/cafe.webp',
      },
      {
        artist: 'Claude Monet',
        name: 'Impression, Sunrise',
        path: '/paintings/impression.webp',
      },
      {
        artist: 'Leonardo da Vinci',
        name: 'Lady with an Ermine',
        path: '/paintings/ermine.webp',
      },
      {
        artist: 'Rembrandt van Rijn',
        name: 'The Storm on the Sea of Galilee',
        path: '/paintings/galilee.webp',
      },
      {
        artist: 'Caspar David Friedrich',
        name: 'Wanderer above the Sea of Fog',
        path: '/paintings/sea.webp',
      },
      {
        artist: 'Vincent van Gogh',
        name: 'Irises',
        path: '/paintings/irises.webp',
      },
      {
        artist: 'Raphael',
        name: 'The Transfiguration',
        path: '/paintings/transfiguration.webp',
      },
      {
        artist: 'Katsushika Hokusai',
        name: 'The Great Wave Off Kanagawa',
        path: '/paintings/wave.webp',
      },
      {
        artist: 'Claude Monet',
        name: 'The Woman with a Parasol',
        path: '/paintings/parasol.webp',
      },
      {
        artist: 'Raphael',
        name: 'Self Portrait',
        path: '/paintings/self.webp',
      },
      {
        artist: 'Pierre-Auguste Renoir',
        name: 'Luncheon of the Boating Party',
        path: '/paintings/pierre.webp',
      },
      {
        artist: 'Rembrandt van Rijn',
        name: 'The Anatomy Lesson of Dr Nicolaes Tulp',
        path: '/paintings/ew.webp',
      },
      {
        artist: 'Jacques-Louis David',
        name: 'Oath of the Horatii',
        path: '/paintings/sword.webp',
      },
      {
        artist: 'Pablo Picaso',
        name: 'The Old Guitarist',
        path: '/paintings/guitarist.webp',
      },
    ]

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
