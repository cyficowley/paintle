<template>
  <div class="mx-auto bg-white">
    <div class="text-5xl text-gray-500 mx-auto pb-4">
      <p>Directions</p>
    </div>
    <div class="text-2xl text-gray-400">
      <p>
        The point of this game is to
        <span class="font-bold">guess the painting</span> by either its
        <span class="italic">artist</span> or
        <span class="italic">name</span> in the
        <span class="font-bold">fewest guesses possible</span>.
      </p>
      <br />
      <p>
        In order to start guessing, you have to
        <span class="font-bold">select a tile</span> on the image to reveal the
        image's first clue.
      </p>
      <br />
      <p>
        Note: You have <span class="font-bold">16 guesses</span> (enough to
        reveal all 16 tiles of the image).
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DirectionsItem',
}
</script>