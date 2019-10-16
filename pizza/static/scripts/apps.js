var EmptyFieldController = (function() {

    document.getElementById("multiplepizzaform").addEventListener("submit", proccess_multiple_pizzas);
    function proccess_multiple_pizzas() {
        //this code checks whether all toppings and sizes fields are empty. if so, prompts warning

        // number of pizzas from Get Pizzas button  on order.html
        let number_of_pizzas = document.getElementById("id_form-TOTAL_FORMS").value;

        // pizza elements
        let pizza_elements = ["topping1", "topping2", "size"];

        // each pizza array. this will save each field ElementById
        var each_pizza_array = [];

        for (let i = 0; i < number_of_pizzas ; i++) {
            pizza_elements.forEach(function(item) {
                let each_pizza = "id_form-" + i + "-" + item;
                each_pizza_array.push(document.getElementById(each_pizza).value);
            });
        }

        console.log(each_pizza_array);

        //if all fields are empty, returns true.
        function isEmpty(topping_and_size) {
            return topping_and_size == "";
        }

        console.log(each_pizza_array.every(isEmpty));

        if(each_pizza_array.every(isEmpty)) {
            alert("Fields are Empty. Please, fill them all");
        }
    }

})();