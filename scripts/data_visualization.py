from tkinter import Y
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from scripts.visualization_logger import logger

class Data_Viz:
    """
    Data visualization 
    """
    #logger.info('Data visualization function succesfully initialized!!!')

    def plot_box(self, df:pd.DataFrame, columns, color:str)->None:
        """
        Boxplot plotting function.
        """
        fig = plt.figure(figsize =(10, 7))
        
        for col in columns:
            # Creating plot
            plt.boxplot(df[columns])
            plt.title(f'Plot of {col}', size=20, fontweight='bold')
            ax = plt.gca()
            ax.set_ylim(top = df[col].quantile(0.9999))
            ax.set_ylim(bottom = 0)
            # show plot
            plt.show()

        #logger.info('Box1 plotting successfuly done!!!')

    def plot_box2(self, df:pd.DataFrame, col:str)->None:
        """
        Boxplot plotting function.
        """
        plt.boxplot(df[col])
        plt.title(f'Plot of {col}', size=20, fontweight='bold')
        ax = plt.gca()
        # show plot
        plt.show()

        #logger.info('Box2 plotting successfuly done!!!')

    def plot_pie(self, df, col, title):
        """
        pie chart plotting function.
        """
        # Wedge properties
        wp = { 'linewidth' : 1, 'edgecolor' : "black" }

        # Creating autocpt arguments
        def func(pct, allvalues):
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)
        
        fig, ax = plt.subplots(figsize =(10, 7))
        wedges, texts, autotexts = ax.pie(df[col[1]],
                                    autopct = lambda pct: func(pct, df[col[1]]),
                                    labels = df[col[0]].to_list(),
                                    startangle = 90,
                                    wedgeprops = wp,)

        plt.setp(autotexts, size = 8, weight ="bold")
        ax.set_title(title)

        #logger.info('Pie plotting successfuly done!!!')


    def showDistribution(self, df, cols):
        """
        Distribution plotting function.
        """
        for index in range(len(cols)):
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(8, 4)) 
            sns.displot(data=df, x=cols[index], kde=True, height=4, aspect=2)
            plt.title(f'Distribution of '+cols[index]+' data volume', size=20, fontweight='bold')
            plt.show()
        
        #logger.info('Distribution showing successfuly done!!!')


    def summ_columns(self, df, unique=True):
        """
        shows columns and their missing values along with data types.
        """
        df2 = df.isna().sum().to_frame().reset_index()
        df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df2['missing_percent_(%)'] = round(df2['missing_count']*100/df.shape[0])
        data_type_lis = df.dtypes.to_frame().reset_index()
        df2['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df2.shape[0]):
                unique_val.append(len(pd.unique(df[df2.iloc[i,0]])))
            df2['unique_values'] = pd.Series(unique_val)

        #logger.info('Summing columns successfuly done!!!')

        return df2


    
    def percent_missing(df: pd.DataFrame):

        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        print("The dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

        #logger.info('Finding out the missing values successfuly done!!!')


    def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
        sns.displot(data=df, x=column, color=color, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.xticks(rotation=90)
        plt.show()

        #logger.info('Histogram plotting successfuly done!!!')

    def plot_count(df:pd.DataFrame, column:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.xticks(rotation=90)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

        #logger.info('Count plotting successfuly done!!!')

    def plot_bar(self, x_ax, y_ax, dfs, titles, axes ):
        """
        plots bar charts
        """
        for i in range(len(axes)):
            sns.barplot(x=x_ax[i], y=y_ax[i], data=dfs[i], ax=axes[i]).set_title(titles[i])

        plt.show()

        #logger.info('Bar plotting successfuly done!!!')
    
    def plot_line(self, df, x, y, figsize, title, name):
        plt.figure(figsize=(figsize[0],figsize[1]))
        sns.lineplot(x = x, y=y, data=df)
        plt.title(title)
        plt.savefig("../charts/"+name)
        plt.show()

        #logger.info('Line plotting successfuly done!!!')