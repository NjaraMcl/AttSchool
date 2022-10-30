
var sidebar = document.getElementsByClassName('nj-sidebar'),
    mainHeader = document.getElementsByClassName('nj-header'),
    mobileNavTrigger = document.getElementsByClassName('nj-header-trigger');

function toggleSidebar(ref) {
    document.getElementById("nj-header-trigger").classList.toggle('change');
    document.getElementById("nj-sidebar").classList.toggle('is-visible');
}