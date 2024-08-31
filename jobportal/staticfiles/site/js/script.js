document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.popup-extra').addEventListener('click', function() {
        // Load gallery content
        var galleryContent = `
            <div class="col-md-4">
                <img src="path_to_image1.jpg" class="img-fluid" alt="Gallery Image 1">
            </div>
            <div class="col-md-4">
                <img src="path_to_image2.jpg" class="img-fluid" alt="Gallery Image 2">
            </div>
            <div class="col-md-4">
                <img src="path_to_image3.jpg" class="img-fluid" alt="Gallery Image 3">
            </div>
            <!-- Add more images as needed -->
        `;
        document.getElementById('mediumGalleryContent').innerHTML = galleryContent;
        
        // Show the modal
        $('#mediumGalleryModal').modal('show');
        



    });
    $(document).ready(function() {
        var videoIndex = 0;
        var videos = [];
    
        $('.view-reel-link').on('click', function(event) {
            event.preventDefault();
            
            // Get the video URLs from the data attribute
            videos = $(this).data('videos');
            videoIndex = 0;
            
            // Load the first video
            loadVideo(videos[videoIndex]);
            
            // Update the navigation section
            updateNavSection(videos.length);
            
            // Show the modal
            $('#reelVideoModal').modal('show');
        });
    
        $('#reelVideoModal').on('hidden.bs.modal', function() {
            // Pause and reset video player
            $('#reelVideoPlayer')[0].pause();
            $('#reelVideoPlayer source').attr('src', '');
            $('#reelVideoPlayer')[0].load();
        });
    
        $('#reelVideoPlayer').on('ended', function() {
            videoIndex++;
            if (videoIndex < videos.length) {
                loadVideo(videos[videoIndex]);
            } else {
                $('#reelVideoModal').modal('hide');
            }
            updateNavDots(videoIndex);
        });
    
        function loadVideo(videoUrl) {
            var videoPlayer = $('#reelVideoPlayer')[0];
            var videoSource = $('#reelVideoPlayer source');
    
            videoSource.attr('src', videoUrl);
            videoPlayer.load();
            videoPlayer.play();
        }
    
        function updateNavSection(numVideos) {
            var navSection = $('#navSection');
            navSection.empty();
            for (var i = 0; i < numVideos; i++) {
                var navDot = $('<div class="nav-dot"></div>');
                if (i === 0) {
                    navDot.addClass('active');
                }
                navSection.append(navDot);
            }
        }
    
        function updateNavDots(index) {
            $('#navSection .nav-dot').removeClass('active');
            $('#navSection .nav-dot').eq(index).addClass('active');
        }
    });
    
    // Close the modal when the background is clicked







});
