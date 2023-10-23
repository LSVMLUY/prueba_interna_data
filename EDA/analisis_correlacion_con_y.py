import pandas as pd
import matplotlib.pyplot as plt





def analisis_correlacion_con_y(data):
    def plot_mean_y_for_bins_in_grid(variable, ax, bins=10):
        # Create bins for the variable
        bins = pd.cut(data[variable], bins=bins)
        # Compute mean of y for each bin
        mean_y_per_bin = data.groupby(bins)['y'].mean()
        # Get the left edge of each bin as x labels
        x_labels = mean_y_per_bin.index.map(lambda x: x.left)
        # Plot with custom x labels
        mean_y_per_bin.plot(kind='bar', color='lightcoral', ax=ax)
        correlation_value = correlations_with_y[variable]
        ax.set_title(f'{variable}\nCorrelation: {correlation_value:.3f}',fontsize=20)
        ax.set_ylabel('Mean of y')
        ax.set_xlabel('')
        # Set custom x labels
        ax.set_xticklabels(x_labels, rotation=80, fontsize=14)
        ax.grid(axis='y')
    # Calculate the correlation matrix
    correlation_matrix = data.corr()

    # Extract correlations with the target variable "y"
    correlations_with_y = correlation_matrix["y"].sort_values(ascending=False)

    # Select the top 20 variables with the strongest correlations (either positive or negative) with "y"
    top_12_vars = correlations_with_y.index[1:13]  # Exclude "y" itself
    bottom_12_vars = correlations_with_y.index[-13:]  

    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(20, 20))
    fig.suptitle('Mean of y for Bins of Top 12 Variables', fontsize=20, y=1.03)
    
    # Plot for the top 20 variables in the grid
    for var, ax in zip(top_12_vars, axes.ravel()):
        plot_mean_y_for_bins_in_grid(var, ax)
        
    plt.tight_layout()
    plt.show()
    
    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(20, 20))
    fig.suptitle('Mean of y for Bins of Bottom 12 Variables', fontsize=20, y=1.03)
    
    # Plot for the top 20 variables in the grid
    for var, ax in zip(bottom_12_vars, axes.ravel()):
        plot_mean_y_for_bins_in_grid(var, ax)
        
    plt.tight_layout()
    plt.show()