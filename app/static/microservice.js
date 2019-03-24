let $target = $("#target");

$(".list-group-item").hover(
    () => {
        $(this).addClass("active");
        console.log("HELLO")
    },
    () => $(this).removeClass("active")
)
let counter = 0
$("#clickme").click(
    ()=> $.ajax({
        type: "GET",
        url: "/api/data",
        success: (response) => {
            console.log(response);
            $.each(response["messages"], function (i, val) { 
                $target.append(
                    '<tr class="table-row"><th scope="row">' + counter +'</th><td>'+ val + '</td></tr>'
                    );
                counter += 1;
            });
        }
    })
)
