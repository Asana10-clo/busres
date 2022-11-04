const dropdown = document.getElementById("dropdown")
const trigger = document.getElementById("dropdown-trigger")
trigger.addEventListener('click', toggleDropdown, false)
  
function toggleDropdown() {
    dropdown.classList.toggle('hidden')
}
