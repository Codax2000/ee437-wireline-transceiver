import pandas as pd
import matplotlib.pyplot as plt


def get_data():
    path_1 = "./equalization_specs_3tap_0pre.csv"
    path_2 = "./equalization_specs_3tap_1pre.csv"
    path_3 = "./equalization_specs_4tap_0pre.csv"
    path_4 = "./equalization_specs_4tap_1pre.csv"

    df1 = pd.read_csv(path_1)
    df1['n_taps'] = 3
    df1['n_precursor_taps'] = 0

    df2 = pd.read_csv(path_2)
    df2['n_taps'] = 3
    df2['n_precursor_taps'] = 1

    df3 = pd.read_csv(path_3)
    df3['n_taps'] = 4
    df3['n_precursor_taps'] = 0

    df4 = pd.read_csv(path_4)
    df4['n_taps'] = 4
    df4['n_precursor_taps'] = 1

    return pd.concat([df1, df2, df3, df4], ignore_index=True)


def plot_data(data):
    fig, ax_grid = plt.subplots(2, 2, subplot_kw={"projection": "3d"}, figsize=(12, 12))
    for i in range(3, 5):
        for j in range(0, 2):
            ax = ax_grid[i-3, j]
            filt_taps = data['n_taps'] == i
            filt_prec = data['n_precursor_taps'] == j
            filt = filt_taps & filt_prec
            data_filtered = data[filt]
            ax.scatter(data_filtered['DC_gain'], data_filtered['Peak_gain'], data_filtered['eye_height'])
            ax.set_title(f"{i} taps, {j} pre-cursor tap")
            ax.set_xlabel("DC Gain [dB]")
            ax.set_ylabel("Peaking Gain [dB]")
            ax.set_zlabel("Eye Opening [V]")
            fig.savefig('Eye Height with Configurations')


def plot_best_data(data):
    filt1 = data['n_taps'] == 3
    filt2 = data['n_precursor_taps'] == 0
    filt3 = data['Peak_gain'] > 5
    filt4 = data['eye_height'] > 0.15
    filt5 = data['Peak_gain'] <= 9.2
    data_filtered = data[filt1 & filt2 & filt3 & filt4 & filt5]
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(7, 7))
    ax.scatter(data_filtered['DC_gain'], data_filtered['Peak_gain'], data_filtered['eye_height'])
    ax.set_title(f"3-Tap Eye Opening vs. Parameters")
    ax.set_xlabel("DC Gain [dB]")
    ax.set_ylabel("Peaking Gain [dB]")
    ax.set_zlabel("Eye Opening [V]")
    fig.savefig("Best Eye Heights.png")

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter('Peak_gain', 'eye_height', data=data_filtered)
    ax.set_xlabel('Peak Gain [dB]')
    ax.set_ylabel('Eye Height [V]')
    fig.savefig('Zoomed In Eye Heights.png')

def main():
    data = get_data()
    plot_data(data)
    plot_best_data(data)


if __name__ == '__main__':
    main()