document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.popup-extra').addEventListener('click', function() {
        loadGalleryContent();
        $('#mediumGalleryModal').modal('show');
    });

    document.getElementById('addMoreImages').addEventListener('click', function() {
        addExtraImages();
    });

    document.getElementById('editGallery').addEventListener('click', function() {
        editGallery();
    });

    function loadGalleryContent() {
        var userProfilePicUrl = "{{user.profile_pic.url}}";
        var galleryContent = `
            <div class="col-md-4">
                <img src="${userProfilePicUrl}" class="img-fluid" alt="Gallery Image 1">
            </div>
            <div class="col-md-4">
                <img src="${userProfilePicUrl}" class="img-fluid" alt="Gallery Image 2">
            </div>
            <div class="col-md-4">
                <img src="${userProfilePicUrl}" class="img-fluid" alt="Gallery Image 3">
            </div>
            <!-- Add more images as needed -->
        `;
        document.getElementById('mediumGalleryContent').innerHTML = galleryContent;

        displayContainerGallery(userProfilePicUrl);
    }

    function addExtraImages() {
        var userProfilePicUrl = "{{user.profile_pic.url}}";
        var extraImages = `
            <div class="col-md-4">
                <img src="${userProfilePicUrl}" class="img-fluid" alt="Gallery Image 4">
            </div>
            <div class="col-md-4">
                <img src="path_to_image5.jpg" class="img-fluid" alt="Gallery Image 5">
            </div>
            <div class="col-md-4">
                <img src="path_to_image6.jpg" class="img-fluid" alt="Gallery Image 6">
            </div>
        `;
        document.getElementById('mediumGalleryContent').insertAdjacentHTML('beforeend', extraImages);
    }

    function editGallery() {
        var images = document.querySelectorAll('#mediumGalleryContent img');
        images.forEach(function(image) {
            image.classList.toggle('selectable');
            image.addEventListener('click', function() {
                this.classList.toggle('selected');
            });
        });

        var editOptions = `
            <button type="button" class="btn btn-danger" id="removeSelectedImages">Remove Selected Images</button>
            <button type="button" class="btn btn-warning" id="selectAllImages">Select All Images</button>
        `;
        document.querySelector('.modal-footer').insertAdjacentHTML('afterbegin', editOptions);

        document.getElementById('removeSelectedImages').addEventListener('click', function() {
            var selectedImages = document.querySelectorAll('#mediumGalleryContent img.selected');
            selectedImages.forEach(function(image) {
                image.parentElement.remove();
            });
        });

        document.getElementById('selectAllImages').addEventListener('click', function() {
            images.forEach(function(image) {
                image.classList.add('selected');
            });
        });
    }

    function displayContainerGallery(userProfilePicUrl) {
        var container = document.getElementById('galleryContainer');
        if (container) {
        var containerGallery = `
            <div class="container-gallery">
                <div class="popup popup-1">
                    <img class="img-responsive" alt="Pop Up Gallery" src="${userProfilePicUrl}" />
                </div>
                <div class="popup popup-2">
                    <img class="img-responsive" alt="Pop Up Gallery" src="path_to_image2.jpg" />
                </div>
                <div class="popup popup-3">
                    <img class="img-responsive" alt="Pop Up Gallery" src="path_to_image3.jpg" />
                </div>
                <div class="popup popup-extra">
                    <img class="img-responsive" alt="More" src="" />
                </div>
            </div>
        `;
        container.innerHTML = containerGallery;
    } 
    else {
        console.error('Container with ID "galleryContainer" not found');
    }
}
});

function addAddressFields() {
    // Create a new div element
    var newDiv = document.createElement("div");
    newDiv.className = "form-group row";
    
    // Create the address input field
    var addressDiv = document.createElement("div");
    addressDiv.className = "col-sm-6";
    var addressInput = document.createElement("input");
    addressInput.type = "text";
    addressInput.name = "address";
    addressInput.id = "address";
    addressInput.className = "form-control";
    addressInput.placeholder = "Address";
    addressDiv.appendChild(addressInput);
    
    // Create the city input field
    var cityDiv = document.createElement("div");
    cityDiv.className = "col-sm-6";
    var cityInput = document.createElement("input");
    cityInput.type = "text";
    cityInput.name = "city";
    cityInput.id = "city";
    cityInput.className = "form-control";
    cityInput.placeholder = "City";
    cityDiv.appendChild(cityInput);
    
    // Append the new input fields to the new div
    newDiv.appendChild(addressDiv);
    newDiv.appendChild(cityDiv);
    
    // Append the new div to the form
    var form = document.getElementById("form-container");
    form.appendChild(newDiv);

    // Move the "Add Address" button to the next line
    // var addButton = document.getElementById("add-address-button");
    // form.appendChild(addButton);
}

function saveAddress() {
    var address = document.getElementById("address").value;
    var city = document.getElementById("city").value;
    
    if (address && city) {
        alert('Address saved: ' + address + ', ' + city);
    } else {
        alert('Please fill in both the address and city fields.');
    }
}


$(document).ready(function() {
    var videoIndex = 0;
    var videos = [];

    $('.view-reel-link').on('click', function(event) {
        event.preventDefault();
        
        // Get the video URLs from the data attribute
        var videoUrls = $(this).data('videos');
        if (typeof videoUrls === 'string') {
            videos = JSON.parse(videoUrls);
        } else {
            videos = videoUrls;
        }
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
        
        // Play the video when it can play
        $('#reelVideoPlayer').off('canplay').on('canplay', function() {
            videoPlayer.play();
        });
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
