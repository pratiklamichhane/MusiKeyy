function formatDuration(time) {
  const minutes = Math.floor(time / 60);
  const seconds = Math.floor(time % 60);
  const formattedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
  return `${minutes}:${formattedSeconds}`;
}

document.addEventListener("DOMContentLoaded", function () {
  let pausedTime = {}; 

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

    audioFile.addEventListener("ended", function () {
      const currentAudio = this;
      const nextAudio =
        currentAudio.parentElement.nextElementSibling.nextElementSibling
          .querySelector("audio");

      if (nextAudio) {
        const playButtons = document.querySelectorAll(
          ".ri-play-circle-fill, .ri-pause-circle-fill"
        );
        playButtons.forEach((playBtn) => {
          playBtn.classList.remove("ri-pause-circle-fill");
          playBtn.classList.add("ri-play-circle-fill");
        });

        nextAudio.play();
      }
    });

    audioFile.addEventListener("timeupdate", function () {
      if (this.paused) {
        pausedTime[this.id] = this.currentTime; 
      }
    });
  });

  const playButtons = document.querySelectorAll(
    ".ri-play-circle-fill, .ri-pause-circle-fill"
  );

  playButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const isPlaying = button.classList.contains("ri-pause-circle-fill");

      const audioFiles = document.querySelectorAll(".audio-file audio");
      audioFiles.forEach((audio) => {
        if (audio !== button.nextElementSibling.querySelector("audio")) {
          audio.pause();
        }
      });

      const audioFile = button.nextElementSibling.querySelector("audio");

      if (!isPlaying) {
        button.classList.remove("ri-play-circle-fill");
        button.classList.add("ri-pause-circle-fill");

        if (audioFile) {
          if (pausedTime.hasOwnProperty(audioFile.id)) {
            audioFile.currentTime = pausedTime[audioFile.id];
          }
          audioFile.play();
        }
      } else {
        button.classList.remove("ri-pause-circle-fill");
        button.classList.add("ri-play-circle-fill");

        if (audioFile) {
          pausedTime[audioFile.id] = audioFile.currentTime;
          audioFile.pause();
        }
      }
    });
  });
});

