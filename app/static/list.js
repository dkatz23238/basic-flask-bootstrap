$(document).ready(
    $("th").hover(
        () => this.classAdd("table-active"),
        () => this.classRemove("table-active")
    )
)

