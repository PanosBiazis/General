@RestController
@RequestMapping("/api")
public class DataController {

    @Autowired
    private DataModelRepository repository;

    @Autowired
    private MLService mlService;

    @PostMapping("/predict")
    public ResponseEntity<Double> predict(@RequestBody Map<String, Double> features) {
        double prediction = mlService.predict(
            features.get("feature1"),
            features.get("feature2"),
            features.get("feature3")
        );
        return ResponseEntity.ok(prediction);
    }

    @PostMapping("/data")
    public DataModel saveData(@RequestBody DataModel dataModel) {
        return repository.save(dataModel);
    }

    @GetMapping("/data")
    public List<DataModel> getData() {
        return repository.findAll();
    }
}
