const { value: email } = await Swal.fire({
    title: "Input email address",
    input: "email",
    inputLabel: "Your email address",
    inputPlaceholder: "Enter your email address"
});
if (email) {
    Swal.fire(`Entered email: ${email}`);
}