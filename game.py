import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("Type the word: 'fhqwhgads' as fast as you can five times.")
input("Press enter to commence.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word:")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if word.lower() != "fhqwhgads":
        mistakes += 1
print("You made " + str(mistakes) + " mistakes.")
print("Now let's make a chart of your results")
t.sleep(5)

x = [1,2,3,4,5]
y = times
legend = ["1","2","3","4","5"]
plt.plot(x,y)
plt.xticks(x, legend)
plt.ylabel('Time in Seconds')
plt.xlabel('Attempts')
plt.title('Everybody to the limit, everybody fhqwhwawagadsss')
plt.show()