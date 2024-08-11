
document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('categories');
    const apartment_content = document.getElementById('apartment');
    const villa_content = document.getElementById('villa');

    // Function to handle content visibility
    function handleContentVisibility() {
        const selectedValue = select.value;
        apartment_content.classList.toggle('d-none', selectedValue !== 'Apartment');
        apartment_content.classList.toggle('d-flex', selectedValue === 'Apartment');
        villa_content.classList.toggle('d-none', selectedValue !== 'Villa');
        villa_content.classList.toggle('d-flex', selectedValue === 'Villa'); 
    }

    handleContentVisibility();

    select.addEventListener('change', handleContentVisibility);
});