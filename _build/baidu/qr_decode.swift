import Foundation
import Vision
import AppKit
for path in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("\(path)\tLOAD_FAIL"); continue }
    let req = VNDetectBarcodesRequest()
    req.symbologies = [.qr]
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    let vals = (req.results ?? []).compactMap { $0.payloadStringValue }
    print("\(path)\t\(vals.isEmpty ? "NONE" : vals.joined(separator: " | "))")
}
