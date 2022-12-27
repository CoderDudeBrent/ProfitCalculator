from django.shortcuts import render


def profit(request):
    return render(request, 'profit.html')


def calculate_profit(request):
    if request.method == 'POST':

        # Get the values entered into the input boxes
        miles_driven = request.POST['miles_driven']
        average_mpg = request.POST['average_mpg']
        payment = request.POST['payment']

        average_fuel_cost = 3.10

        if miles_driven == '' or average_mpg == '' or payment == '':
            error_message = "Please fill every entry."
            return render(request, 'profit.html', {'error_message': error_message})

        # Calculate the profit
        profit = float(payment) - (float(miles_driven) /
                                   float(average_mpg)) * float(average_fuel_cost)

        # Round the profit to 2 decimal places
        profit = format(profit, '.2f')

        # pass to template

        context = {
            'profit': profit
        }

    return render(request, 'profit.html', context)
