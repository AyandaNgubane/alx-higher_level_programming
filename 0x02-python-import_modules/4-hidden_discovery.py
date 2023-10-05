#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    h_names = dir(hidden_4)

    for i in range(len(h_names)):
        if (h_names[i][0:2] != "__"):
            print(h_names[i])
