function confirmarDelete(id) {
    Swal.fire({
        title: "estas segr@?",
        text: "Una vez borrado no hay vuelta atras",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "BORRAR"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Borrado! La Id de periodista afecta do es " + id,
                text: "El periodista ah sido borrado exitosamente",
                icon: "success"
            }).then(() => {
                document.getElementById('delete-form-' + id).submit(); // Envía el formulario correspondiente
            });
        }
    });
}



