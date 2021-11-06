from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Flight
from django.views import generic


# view: flights list
class FlightIndexView(generic.ListView):
    template_name = 'flights/index.html'
    context_object_name = 'flights_list'

    def get_queryset(self):
        return Flight.objects.all


def check_schedule_arrival_departure(runway_num):
    """
      Description: check schedule arrival-departure all flights have landing place
      param: runway_num - number of runway
      Return value: Boolean (True/False)
    """
    runway_counter = 0
    times_flights_list = list()
    all_flights = Flight.objects.all()
    for flight in all_flights:
        times_flights_list.append({"type": "arrival", "time": flight.arrival})
        times_flights_list.append({"type": "departure", "time": flight.departure})

    times_flights_list = sorted(times_flights_list, key=lambda f: f['time'])

    print("Times list after sort:")
    for flight in times_flights_list:
        if flight['type'] == 'arrival':
            runway_counter += 1
        else:
            runway_counter -= 1
        if runway_counter > runway_num:
            print("check return False: runway_counter={0} while runway_num={1}".format(runway_counter, runway_num))
            return False
        # not expected to get < 0 values:
        elif runway_counter < 0:
            print("check return False: runway_counter={0}".format(runway_counter))
            return False
        print("Flight: {0}".format(flight))
        print("runway_counter={0}".format(runway_counter))

    return True


def schedule_ok(request,):
    """
      Description: schedule ok view
      param: request
      Return:
    """
    runway_num_example = 8

    succeed = check_schedule_arrival_departure(runway_num=runway_num_example)
    print("Results of check_schedule_arrival_departure={}".format(succeed))
    if succeed:
        return HttpResponse('<h1>succeed</h1>')
    else:
        return HttpResponse('<h1>Failed </h1>')