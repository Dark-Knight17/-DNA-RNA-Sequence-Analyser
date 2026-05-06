document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const sequenceTextArea = document.getElementById('sequence');
    const strandSelection = document.getElementById('strand-selection');

    // Drag and Drop Logic
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('drop-zone--over');
    });

    ['dragleave', 'dragend'].forEach(type => {
        dropZone.addEventListener(type, () => {
            dropZone.classList.remove('drop-zone--over');
        });
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            updateThumbnail(dropZone, e.dataTransfer.files[0].name);
        }
        dropZone.classList.remove('drop-zone--over');
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length) {
            updateThumbnail(dropZone, fileInput.files[0].name);
        }
    });

    function updateThumbnail(dropZone, fileName) {
        let prompt = dropZone.querySelector('.drop-zone__prompt');
        prompt.textContent = `Selected: ${fileName}`;
    }

    // Strand Selection Visibility Logic
    sequenceTextArea.addEventListener('input', () => {
        const value = sequenceTextArea.value.toUpperCase();
        if (value.includes('T') && !value.includes('U')) {
            strandSelection.style.display = 'block';
        } else if (value.includes('U')) {
            strandSelection.style.display = 'none';
        } else if (value.trim() === '') {
            strandSelection.style.display = 'none';
        } else {
            // Only A, C, G - could be DNA, show it to be safe
            strandSelection.style.display = 'block';
        }
    });
});
