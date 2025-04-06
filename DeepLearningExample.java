import org.deeplearning4j.datasets.iterator.impl.MnistDataSetIterator;
import org.deeplearning4j.nn.api.OptimizationAlgorithm;
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.conf.layers.ConvolutionLayer;
import org.deeplearning4j.nn.conf.layers.MaxPooling1D;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.optimize.api.IterationListener;
import org.deeplearning4j.optimize.listeners.ScoreIterationListener;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.learning.config.Adam;
import org.nd4j.linalg.lossfunctions.LossFunctions;

public class DeepLearningExample {

    public static void main(String[] args) throws Exception {
        int numInputs = 784;  // MNIST images are 28x28 pixels, so 784 inputs
        int numOutputs = 10;  // 10 classes (digits 0-9)
        int numHiddenNodes = 128;

        // Load MNIST data
        MnistDataSetIterator mnistTrain = new MnistDataSetIterator(64, true, 12345);

        // Build the neural network configuration
        MultiLayerNetwork model = new MultiLayerNetwork(
            new NeuralNetConfiguration.Builder()
                .seed(12345)
                .updater(new Adam(0.001))  // Learning rate
                .list()
                .layer(new DenseLayer.Builder().nIn(numInputs).nOut(numHiddenNodes)
                    .activation(Activation.RELU).build())
                .layer(new OutputLayer.Builder(LossFunctions.LossFunction.NEGATIVELOGLIKELIHOOD)
                    .nIn(numHiddenNodes).nOut(numOutputs)
                    .activation(Activation.SOFTMAX).build())
                .build()
        );
        model.init();

        // Add an iteration listener to see the score
        model.setListeners(new ScoreIterationListener(10));

        // Train the model
        for (int epoch = 0; epoch < 10; epoch++) {
            model.fit(mnistTrain);
            System.out.println("Epoch " + epoch + " complete");
        }

        // Evaluate the model here, e.g., on the test set
    }
}
