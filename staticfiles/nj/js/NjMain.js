
var sidebar = document.getElementsByClassName('nj-sidebar'),
    mainHeader = document.getElementsByClassName('nj-header'),
    mobileNavTrigger = document.getElementsByClassName('nj-header-trigger'),
    submenu = document.getElementsByClassName('has_child');

function toggleSidebar(ref) {
    document.getElementById("nj-header-trigger").classList.toggle('change');
    document.getElementById("nj-sidebar").classList.toggle('is-visible');
}
function myFunction(ref) {
    document.getElementById("nj-sub-side-list").classList.toggle('is_visible');
}