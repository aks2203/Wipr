################################
#
# Avi Schwarzschild, Dan Singer
# DevFest 2017
# Wipr
# Weather module
# for getting foracasts at a time and place.
#
################################



import forecastio
from datetime import datetime, timedelta
import os

api_key = '45cd7693234cd1549f8d103703b7b5da'

def get_weather(lat, lng, time=datetime.now()):
    forecast = forecastio.load_forecast(api_key, lat, lng, time)
    current = forecast.currently()
    return current.summary, current.icon
    # return current.icon

# def weather_report(timed_markers, time=datetime.now()):
#     forcasts = []
#     for marker in timed_markers:
#         forcasts.append(get_weather(marker[0], marker[1], time=(time+ timedelta(seconds=marker[2]))))
    
#     header = '''\documentclass{resume}
#                 \usepackage[left=0.3in,top=0.3in,right=0.3in,bottom=0.25in]{geometry}'''

#     table = '''
#             \begin{center}
#             \begin{tabular}{ c c c }
#             '''
#     for i in xrange(len(forcasts)):
#         table += str(timed_markers[i][2])#, + str(forcasts[i][0]) + str(forcasts[i][0]) + '\\'
#     table += '\end{tabular} \end{center}'

#     fh = open('report.tex', 'w+')
#     fh.write(header)
#     fh.write(table)
#     fh.close()

#     os.system('pdflatex report.tex report.pdf')


