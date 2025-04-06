@Entity
public class DataModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private double feature1;
    private double feature2;
    private double feature3;
    private double accuracy;

    // Getters and setters
}
