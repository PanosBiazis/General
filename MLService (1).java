@Service
public class MLService {
    public double predict(double feature1, double feature2, double feature3) {
        return feature1 * 0.5 + feature2 * 0.3 + feature3 * 0.2;
    }
}
