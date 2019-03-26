$(document).ready(
    $("th").hover(
        () => $(this).addClass("table-primary"),
        () => $(this).removeClass("table-primary")
    )
)

