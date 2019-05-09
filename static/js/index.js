'use strict';
$(window).ready(() => {

    $(".run-tests").on("click", ev => {
            let button = ev.currentTarget;
            let perform_post = true;

            let enableButton = () => { button.removeAttribute("disabled") };

            // Disable the button to prevent multiple concurrent requests
            button.setAttribute("disabled", true);

            // Check which methods were selected
            let selected_methods = document.querySelectorAll(".method-check:checked");

            if( selected_methods.length === 0 ){

                alert("You need to select at least one method to test");

                perform_post = false;

                enableButton();

            }

            let num_items = document.getElementById("num-items").value;

            if( num_items > 1000000 || num_items < 1 ){
                alert("The number of items must be between 1 and 100000");
                perform_post = false;
                enableButton();
            }

            if( perform_post ){
                let free_status = () => { $("#status").css("color", "green").html("available") };

                $("#status").css("color", "red").html("busy");

                for( let x = 0; x < selected_methods.length ; x++ ){

                    let method = selected_methods[x];

                    $.post("run_method.py", {"method": method.value, "items": num_items}, response => {
                        try {
                            var response_json = JSON.parse(response);
                        } catch(e) {
                            alert("There was an error reading the json output. Contact the developer if this happens often.");
                            return;
                        }
                       if( response_json.status ){
                           // Append the results
                           $("#results").append(
                               "<p><a class='red'>" +
                               method.value +
                               "</a> took <a class='green'>" +
                               response_json.payload +
                               "</a> seconds with <a class='blue'>" +
                               num_items +
                               "</a> items.</p>"
                           );
                       } else {

                           for( let y = 0 ; y < response_json.errors.length ; y++ ){
                               alert(response_json.errors[y]);
                           }

                       }

                       if( x === selected_methods.length - 1 ){
                           free_status();
                           enableButton();
                       }

                    }).fail( failure => {

                        console.log(failure);

                        alert("There was an error performing that request. Please try again or contact the developer if this continues." +
                            "\nError code: " + failure.status +
                            "\nError Text: "+ failure.statusText
                        );

                        free_status();
                        enableButton();

                    });

                }

            }

        }
    );

});