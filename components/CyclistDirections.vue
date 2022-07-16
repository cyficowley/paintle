<template>
    <div class="mx-auto bg-white">
        <div class="text-2xl sm:text-5xl text-gray-500 mx-auto pb-4">
            <p>Directions</p>
        </div>
        <div class="text-lg sm:text-2xl text-gray-400">
            <p>
                The point of this game is to
                <span class="font-bold">guess the cyclist</span> based on the
                photo in the <span class="font-bold">fewest guesses
                    possible</span>.
            </p>
            <br />
            <p>
                In order to start guessing, you have to
                <span class="font-bold">select a tile</span> on the image to
                reveal the image's first clue.
            </p>
            <br />
            <p>
                Note 1: You have <span class="font-bold">16 guesses</span>
                (enough to
                reveal all 16 tiles of the image).
            </p>
            <br />
            <p>
                Note 2: After your <span class="font-bold">16 guesses</span>, if
                you still don't know the answer, an "Idk" button will appear in
                red
                next to "Submit" and you can click that to "give up" and reveal
                the
                answer.
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CyclistDirectionsItem',
}
</script>
