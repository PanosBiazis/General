#include <windows.h>

// Window Procedure function declaration
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    // Register the window class
    const char CLASS_NAME[] = "ColorfulShapesWindowClass";

    WNDCLASS wc = { };

    wc.lpfnWndProc   = WindowProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hCursor       = LoadCursor(NULL, IDC_ARROW);

    RegisterClass(&wc);

    // Create the window
    HWND hwnd = CreateWindowEx(
        0,                              // Optional window styles
        CLASS_NAME,                     // Window class
        "Colorful Shapes",              // Window text
        WS_OVERLAPPEDWINDOW,            // Window style
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 400, // Size and position
        NULL,       // Parent window
        NULL,       // Menu
        hInstance,  // Instance handle
        NULL        // Additional application data
    );

    if (hwnd == NULL) {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);

    // Run the message loop
    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            // Draw a red rectangle
            HBRUSH redBrush = CreateSolidBrush(RGB(255, 0, 0));
            RECT rect = {50, 50, 150, 150};
            FillRect(hdc, &rect, redBrush);
            DeleteObject(redBrush);

            // Draw a blue ellipse (oval)
            HBRUSH blueBrush = CreateSolidBrush(RGB(0, 0, 255));
            SelectObject(hdc, blueBrush);
            Ellipse(hdc, 200, 50, 300, 150);
            DeleteObject(blueBrush);

            // Draw a green line
            HPEN greenPen = CreatePen(PS_SOLID, 5, RGB(0, 255, 0));
            SelectObject(hdc, greenPen);
            MoveToEx(hdc, 50, 200, NULL);
            LineTo(hdc, 150, 300);
            DeleteObject(greenPen);

            // Draw a yellow triangle (polygon)
            HBRUSH yellowBrush = CreateSolidBrush(RGB(255, 255, 0));
            POINT points[] = {{250, 200}, {300, 300}, {350, 200}};
            SelectObject(hdc, yellowBrush);
            Polygon(hdc, points, 3);
            DeleteObject(yellowBrush);

            // Draw a purple arc
            HPEN purplePen = CreatePen(PS_SOLID, 5, RGB(128, 0, 128));
            SelectObject(hdc, purplePen);
            Arc(hdc, 50, 350, 150, 450, 50, 400, 150, 400);
            DeleteObject(purplePen);

            EndPaint(hwnd, &ps);
        }
        return 0;

        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
    }

    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
// Explanation:
// WinMain: The entry point for Windows applications. It initializes the application and creates the main window.
// WNDCLASS and CreateWindowEx: Used to define and create the window.
// WindowProc: The window procedure that handles messages like WM_PAINT (where drawing happens) and WM_DESTROY (which handles cleanup and exit).
// WM_PAINT: A message sent to the window when it needs to be redrawn. This is where drawing operations are performed using the GDI (Graphics Device Interface).
// HDC (Handle to Device Context): Used to draw on the window.
// RGB(): Creates a color from red, green, and blue components.
// HBRUSH and HPEN: Used to define how shapes and lines are filled and outlined.
// When you run this code, a window will appear with colorful shapes, including a red rectangle, a blue oval, a green line, a yellow triangle, and a purple arc.