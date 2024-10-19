async function showAddBookModal() {
    document.querySelector("#modal").classList.remove("hidden");
  
    document.getElementById("confirm-modal").onclick = async function () {
        await addBook();
        closeModal();
    };
  }
  
  function closeModal() {
    document.querySelector("#form").reset();
    window.location.href="/explore";
    document.querySelector("#modal").classList.add("hidden");
  }
  
  function submitFilterForm() {
    var form = document.getElementById('filterForm');
    form.addEventListener('submit', function() {
      form.reset();
    });
    form.submit();
  }
  
  function returnToKatalog(){
    window.location.href="/explore";
  }
  
  document.getElementById("cancel-modal").addEventListener("click", closeModal);