// Function to format duration in mm:ss format
function formatDuration(time) {
  const minutes = Math.floor(time / 60);
  const seconds = Math.floor(time % 60);
  const formattedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
  return `${minutes}:${formattedSeconds}`;
}

document.addEventListener("DOMContentLoaded", function () {
  // Display duration for all audio elements
  const audioFiles = document.querySelectorAll(".audio-file audio");
  audioFiles.forEach((audioFile) => {
    audioFile.addEventListener("loadedmetadata", function () {
      const durationElement =
        audioFile.parentElement.nextElementSibling.querySelector(
          ".song-duration"
        );
      const duration = formatDuration(audioFile.duration);
      durationElement.textContent = duration;
    });
  });

  // Select all elements with the play button class
  const playButtons = document.querySelectorAll(
    ".ri-play-circle-fill, .ri-pause-circle-fill"
  );

  // Add event listeners to each play/pause button
  playButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const isPlaying = button.classList.contains("ri-pause-circle-fill");

      // Pause any other playing audios before playing this one
      const audioFiles = document.querySelectorAll(".audio-file audio");
      audioFiles.forEach((audio) => {
        if (audio !== button.nextElementSibling.querySelector("audio")) {
          audio.pause();
        }
      });

      // Reset all buttons to play state
      playButtons.forEach((playBtn) => {
        playBtn.classList.remove("ri-pause-circle-fill");
        playBtn.classList.add("ri-play-circle-fill");
      });

      if (!isPlaying) {
        // Change the icon to pause
        button.classList.remove("ri-play-circle-fill");
        button.classList.add("ri-pause-circle-fill");

        // Play the audio associated with this button
        const audioFile = button.nextElementSibling.querySelector("audio");
        if (audioFile) {
          audioFile.play();
        }
      } else {
        // Change the icon to play
        button.classList.remove("ri-pause-circle-fill");
        button.classList.add("ri-play-circle-fill");

        // Pause the audio associated with this button
        const audioFile = button.nextElementSibling.querySelector("audio");
        if (audioFile) {
          audioFile.pause();
          audioFile.currentTime = 0; // Resets the audio to the beginning
        }
      }
    });
  });
});
