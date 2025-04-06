package main

import (
	"log"
	"math"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

const (
	screenWidth  = 640
	screenHeight = 480
	carWidth     = 40
	carHeight    = 80
	carSpeed     = 4
)

type Game struct {
	carX, carY float64
	carAngle   float64
	carImage   *ebiten.Image
}

func (g *Game) Update() error {
	if ebiten.IsKeyPressed(ebiten.KeyUp) {
		g.carY -= carSpeed * math.Cos(g.carAngle)
		g.carX += carSpeed * math.Sin(g.carAngle)
	}
	if ebiten.IsKeyPressed(ebiten.KeyDown) {
		g.carY += carSpeed * math.Cos(g.carAngle)
		g.carX -= carSpeed * math.Sin(g.carAngle)
	}
	if ebiten.IsKeyPressed(ebiten.KeyLeft) {
		g.carAngle -= 0.1
	}
	if ebiten.IsKeyPressed(ebiten.KeyRight) {
		g.carAngle += 0.1
	}

	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	opts := &ebiten.DrawImageOptions{}
	opts.GeoM.Translate(g.carX, g.carY)
	opts.GeoM.Rotate(g.carAngle)
	screen.DrawImage(g.carImage, opts)
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
	return outsideWidth, outsideHeight
}

// func main() {
// 	carImage, _, err := ebitenutil.NewImageFromFile("cars.png")
// 	if err != nil {
// 		log.Fatal(err)
// 	}

// 	game := &Game{
// 		carX:     float64(screenWidth / 2),
// 		carY:     float64(screenHeight / 2),
// 		carImage: carImage,
// 	}

// 	ebiten.SetWindowSize(screenWidth, screenHeight)
// 	ebiten.SetWindowTitle("2D Car Game")
// 	if err := ebiten.RunGame(game); err != nil {
// 		log.Fatal(err)
// 	}
// }

func main() {
    path := "cars.png"
    log.Println("Loading image from:", path)
    carImage, _, err := ebitenutil.NewImageFromFile(path)
    if err != nil {
        log.Fatalf("Failed to load image: %v", err)
    }

    game := &Game{
        carX:     float64(screenWidth / 2),
        carY:     float64(screenHeight / 2),
        carImage: carImage,
    }

    ebiten.SetWindowSize(screenWidth, screenHeight)
    ebiten.SetWindowTitle("2D Car Game")
    if err := ebiten.RunGame(game); err != nil {
        log.Fatal(err)
    }
}
