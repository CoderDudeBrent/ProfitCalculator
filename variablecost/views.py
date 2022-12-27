from django.shortcuts import render


def variablecost(request):
    return render(request, 'variablecost.html')


def calculate_v_cost(request):
    if request.method == 'POST':
        # get values for variable cost input fields
        fuel_expense = request.POST.get('fuel_expense')
        maint_expense = request.POST.get('maint_expense')
        repair_expense = request.POST.get('repair_expense')
        other_expense = request.POST.get('other_expense')
        total_miles_driven = request.POST.get('total_miles_driven')

        # calculate total cost and cost per mile

        if fuel_expense == '' or repair_expense == '' or other_expense == '' or total_miles_driven == '':
            error_message = "Please fill in all fields."
            return render(request, 'variablecost.html', {'error_message': error_message})

        else:
            total_cost = int(fuel_expense) + int(maint_expense) + \
                int(repair_expense) + int(other_expense)

            cost_per_mile = total_cost / int(total_miles_driven)

            # pass to template

            context = {
                'total_cost': total_cost,
                'cost_per_mile': cost_per_mile,
            }

    return render(request, 'variablecost.html', context)
