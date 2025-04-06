import weka.core.Instances;
import weka.core.DenseInstance;
import weka.core.Attribute;
import weka.core.FastVector;
import weka.classifiers.functions.LinearRegression;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;

import java.util.Random;

public class LinearRegressionExample {
    public static void main(String[] args) throws Exception {
        // Creating attributes
        FastVector attributes = new FastVector();
        attributes.addElement(new Attribute("x"));
        attributes.addElement(new Attribute("y"));

        // Create an empty dataset with two attributes
        Instances data = new Instances("LinearRegressionData", attributes, 0);
        data.setClassIndex(1);

        // Adding instances (data)
        double[] values1 = new double[]{1, 3};
        double[] values2 = new double[]{2, 5};
        double[] values3 = new double[]{3, 7};
        data.add(new DenseInstance(1.0, values1));
        data.add(new DenseInstance(1.0, values2));
        data.add(new DenseInstance(1.0, values3));

        // Initialize the model and train it
        Classifier model = new LinearRegression();
        model.buildClassifier(data);

        // Evaluate the model
        Evaluation evaluation = new Evaluation(data);
        evaluation.evaluateModel(model, data);
        System.out.println("Model Evaluation: " + evaluation.toSummaryString());
    }
}
