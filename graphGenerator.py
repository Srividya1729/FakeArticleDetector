import plotly
import plotly.graph_objs as go
from plotly.offline import plot,iplot


def generateGraph(filename, labels):
    true = []
    fake = []

    fp = open(filename)
    if 'dummy' in filename:
        fp.readline()
        lines = fp.readlines()
        labFile = open(labels)
        labels = labFile.readlines()
        ttr = []
        stop = []
        sent = []
        contentToNonPoS  = []
        Noun = []
        Verb = []
        adjNoun = []
        for data in lines:
            data = data.strip().split('\t')
            ttr.append(float(data[1]))
            stop.append(float(data[2]))
            sent.append(float(data[3]))
            contentToNonPoS.append(float(data[4]))
            Noun.append(float(data[5]))
            Verb.append(float(data[6]))
            adjNoun.append(float(data[7]))


        # true = []
        # fake = []
        # for i in range(len(ttr)):
        #     if int(labels[i]) == 0:
        #         fake.append(ttr[i])
        #     else:
        #         true.append(ttr[i])
        #
        # trace1 = go.Histogram(x=true, opacity=0.75, name='real')
        # trace2 = go.Histogram(x=fake, opacity=0.75, name='fake')
        #
        # data = [trace1, trace2]
        # layout = go.Layout(barmode='overlay')
        # fig = go.Figure(data=data, layout=layout)

        # plot(fig)


        true = []
        fake = []
        for i in range(len(labels)):
            if int(labels[i]) == 0:
                fake.append(sent[i])
            else:
                true.append(sent[i])

        trace1 = go.Histogram(x=true, opacity=0.75, name='real')
        trace2 = go.Histogram(x=fake, opacity=0.75, name='fake')

        data = [trace1, trace2]
        layout = go.Layout(barmode='overlay')
        fig = go.Figure(data=data, layout=layout)

        plot(fig)


    else:
        data = fp.readlines()
        labFile = open(labels)
        labels = labFile.readlines()

        for i in range(len(data)):
            if int(labels[i]) == 0:
                fake.append(data[i])
            else:
                true.append(data[i])

        trace1 = go.Histogram(x = true, opacity = 0.75, name = 'real')
        trace2 = go.Histogram(x = fake, opacity = 0.75, name = 'fake')

        data = [trace1, trace2]
        layout = go.Layout(barmode='overlay')
        fig = go.Figure(data = data, layout=layout)

        plot(fig)


def main():
    generateGraph('dummy.txt', 'balancedTrainingDataLabels.dat')
    print 'red'


if __name__ == '__main__':
    main()