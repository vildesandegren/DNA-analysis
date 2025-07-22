
import matplotlib.pyplot as plt
import os
import time

def analyze_sequence():
    file_input = input("Input file:")
    with open(file_input, "r") as file:
        a = 0
        t = 0
        g = 0
        c = 0
        total = 0
        for line in file:
            line = line.strip()
            if not line.startswith(">"):
                total += len(line)
                for base in line:
                    if base == "A":
                        a += 1
                    if base == "T":
                        t += 1
                    if base == "C":
                        c += 1
                    if base == "G":
                        g += 1
        print(f"Total bases: {total}")
        print(f"A: {a} ({(a/total*100):.1f}%)")
        print(f"T: {t} ({(t/total*100):.1f}%)")
        print(f"C: {c} ({(c/total*100):.1f}%)")
        print(f"G: {g} ({(g/total*100):.1f}%)")
        print(f"G-C content: {((c + g)/total)*100:.1f}%")

    # graph
    bases = ["A", "T", "C", "G"]
    count = [a, t, c, g]
    plt.bar(bases, count)
    plt.title("Base frequency in DNA-sequence")
    plt.xlabel("Base")
    plt.ylabel("Count")
    save_file = input("Do you want to save the plot as an image? (y/n)")
    if save_file.lower() == "y":
        #make unique name for plot
        base_name = os.path.splitext(file_input)[0]
        timestamp = time.strftime("%d%m%Y-%H%M")
        plot_name = f"{base_name}_plot_{timestamp}"
        
        #place plots in seperate folder       
        folder = "plots"
        os.makedirs(folder, exist_ok=True)
        plot_path = os.path.join(folder, plot_name)

        #save plot and let user know
        plt.savefig(plot_name, format="png")
        print(f"Plot saved as {plot_name}.png")
    #show plot. 
    plt.show()



if __name__ == "__main__":
    analyze_sequence()
